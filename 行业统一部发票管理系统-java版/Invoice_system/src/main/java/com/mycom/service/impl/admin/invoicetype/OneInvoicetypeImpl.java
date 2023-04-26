package com.mycom.service.impl.admin.invoicetype;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.SystemInvoiceTypeEntity;
import com.mycom.mapper.SystemInvoiceTypeMapper;
import com.mycom.service.admin.invoicetype.OneInvoicetypeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

@Service
public class OneInvoicetypeImpl extends ServiceImpl<SystemInvoiceTypeMapper, SystemInvoiceTypeEntity> implements OneInvoicetypeService {
    @Autowired
    SystemInvoiceTypeMapper systemInvoiceTypeMapper;

    @Override
    public LinkedHashMap GetOneInvoicetype(Integer invoicetypeId){

        Map lmp = new LinkedHashMap();
        SystemInvoiceTypeEntity systemInvoiceTypeEntityRusult = systemInvoiceTypeMapper.selectById(invoicetypeId);
        if(systemInvoiceTypeEntityRusult == null){
            lmp.put("code",0);
            lmp.put("info","faid");
            lmp.put("data","数据不存在；");
        }
        else {
            Map lmp0 = new LinkedHashMap();
            lmp0.put("id",systemInvoiceTypeEntityRusult.getId());
            lmp0.put("id",systemInvoiceTypeEntityRusult.getInvoicetypeName());
            lmp.put("code",1);
            lmp.put("info","success");
            lmp.put("data",lmp0);
        }
        return (LinkedHashMap) lmp;
    }
}
