package com.mycom.service.impl.alllist;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.SystemCompanyEntity;
import com.mycom.entity.SystemInvoiceTypeEntity;
import com.mycom.mapper.SystemCompanyMapper;
import com.mycom.service.alllist.ListCompanyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

@Service
public class ListCompanyServiceImpl extends ServiceImpl<SystemCompanyMapper, SystemCompanyEntity> implements ListCompanyService{
    @Autowired
    SystemCompanyMapper systemCompanyMapper;

    @Override
    public LinkedHashMap GetCompanyList(){
        QueryWrapper<SystemCompanyEntity> qw = new QueryWrapper<>();
        List<SystemCompanyEntity> rlist0 = systemCompanyMapper.selectList(qw);
        List rlist = new ArrayList();

        for(int i =0;i<rlist0.size();i++){
            Map lmp0 = new LinkedHashMap();
            lmp0.put("id",rlist0.get(i).getId());
            lmp0.put("user_name",rlist0.get(i).getCompany_name());
            rlist.add(lmp0);
        }
        Map lmp = new LinkedHashMap();
        lmp.put("code",1);
        lmp.put("info","success");
        lmp.put("data",rlist);
        return (LinkedHashMap) lmp;
    }
}
