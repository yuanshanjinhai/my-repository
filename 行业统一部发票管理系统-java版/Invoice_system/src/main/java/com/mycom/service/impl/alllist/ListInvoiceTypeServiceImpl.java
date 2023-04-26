package com.mycom.service.impl.alllist;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.SystemInvoiceTypeEntity;
import com.mycom.mapper.SystemInvoiceTypeMapper;
import com.mycom.service.alllist.ListInvoiceTypeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

@Service
public class ListInvoiceTypeServiceImpl extends ServiceImpl<SystemInvoiceTypeMapper, SystemInvoiceTypeEntity> implements ListInvoiceTypeService {
    @Autowired
    SystemInvoiceTypeMapper systemInvoiceTypeMapper;

    @Override
    public LinkedHashMap GetInvoiceTypeList(){
        QueryWrapper<SystemInvoiceTypeEntity> qw = new QueryWrapper<>();
        List<SystemInvoiceTypeEntity> rlist0 = systemInvoiceTypeMapper.selectList(qw);
        List rlist = new ArrayList();

        for(int i =0;i<rlist0.size();i++){
            Map lmp0 = new LinkedHashMap();
            lmp0.put("id",rlist0.get(i).getId());
            lmp0.put("user_name",rlist0.get(i).getInvoicetypeName());
            rlist.add(lmp0);
        }
        Map lmp = new LinkedHashMap();
        lmp.put("code",1);
        lmp.put("info","success");
        lmp.put("data",rlist);
        return (LinkedHashMap) lmp;
    }
}
