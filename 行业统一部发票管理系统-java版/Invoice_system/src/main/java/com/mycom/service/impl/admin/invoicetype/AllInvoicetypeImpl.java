package com.mycom.service.impl.admin.invoicetype;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.SystemCompanyEntity;
import com.mycom.entity.SystemInvoiceTypeEntity;
import com.mycom.mapper.SystemInvoiceTypeMapper;
import com.mycom.service.admin.invoicetype.AllInvoicetypeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import sun.awt.image.ImageWatched;

import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

@Service
public class AllInvoicetypeImpl extends ServiceImpl<SystemInvoiceTypeMapper,SystemInvoiceTypeEntity> implements AllInvoicetypeService {
    @Autowired
    SystemInvoiceTypeMapper systemInvoiceTypeMapper;

    @Override
    public LinkedHashMap GetAllInvoicetype(SystemInvoiceTypeEntity systemInvoiceTypeEntity){
        QueryWrapper<SystemInvoiceTypeEntity> qw = new QueryWrapper<>();
        List<SystemInvoiceTypeEntity> rlist0 = systemInvoiceTypeMapper.selectList(qw);

        Map lmp = new LinkedHashMap();
        List rlist = new LinkedList();
        if(rlist0.isEmpty() == false){
            for(int i=0;i<rlist0.size();i++){
                Map temLmp = new LinkedHashMap();
                temLmp.put("id",rlist0.get(i).getId());
                temLmp.put("invoicetypeName",rlist0.get(i).getInvoicetypeName());
                rlist.add(temLmp);
            }

        }
        lmp.put("code",1);
        lmp.put("info","success");
        lmp.put("data",rlist);
        return (LinkedHashMap) lmp;
    }
}
