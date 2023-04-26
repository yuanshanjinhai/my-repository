package com.mycom.service.impl.admin.company;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.SystemCompanyEntity;
import com.mycom.mapper.SystemCompanyMapper;
import com.mycom.service.admin.company.AllCompanyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

@Service
public class AllCompanyServiceImpl extends ServiceImpl<SystemCompanyMapper, SystemCompanyEntity> implements AllCompanyService {
    @Autowired
    SystemCompanyMapper systemCompanyMapper;

    @Override
    public LinkedHashMap GetAllCompany(String companyName){
        QueryWrapper<SystemCompanyEntity> qw = new QueryWrapper<>();
        List<SystemCompanyEntity> rlist0;
        List rlist = new ArrayList();
        if(companyName == null){
            rlist0 = systemCompanyMapper.selectList(qw);
        }
        else {
            qw.select("id","company_name","company_abbreviation","company_explain").like("company_name",companyName);
            rlist0 = systemCompanyMapper.selectList(qw);
        }
        System.out.println("rlist0=" +rlist0);
        if(rlist0.isEmpty() == false){
            for(int i =0;i<rlist0.size();i++){
                Map lmp0 = new LinkedHashMap();
                lmp0.put("id",rlist0.get(i).getId());
                lmp0.put("Company_name",rlist0.get(i).getCompany_name());
                lmp0.put("company_abbreviation",rlist0.get(i).getCompany_abbreviation());
                lmp0.put("company_explain",rlist0.get(i).getCompany_explain());
                rlist.add(lmp0);
            }
        }
        Map lmp = new LinkedHashMap();
        lmp.put("code",1);
        lmp.put("info","success");
        lmp.put("data",rlist);
        return (LinkedHashMap) lmp;
    }
}
