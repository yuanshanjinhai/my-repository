package com.mycom.service.impl.admin.invoicetype;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.SystemInvoiceTypeEntity;
import com.mycom.mapper.SystemInvoiceTypeMapper;
import com.mycom.service.admin.invoicetype.InsertInvoicetypeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

@Service
public class InsertInvoicetypeImpl extends ServiceImpl<SystemInvoiceTypeMapper, SystemInvoiceTypeEntity> implements InsertInvoicetypeService {
    @Autowired
    SystemInvoiceTypeMapper systemInvoiceTypeMapper;

    @Override
    public LinkedHashMap InsertInvoicetype(SystemInvoiceTypeEntity systemInvoiceTypeEntity){
        String invoicetypeName = systemInvoiceTypeEntity.getInvoicetypeName();
        String errorStr = "";
        if(invoicetypeName.length() > 30){
            errorStr += "发票类型名称不能超过30个字；";
        }

        QueryWrapper<SystemInvoiceTypeEntity> qw = new QueryWrapper<>();
        List<SystemInvoiceTypeEntity> rlist = systemInvoiceTypeMapper.selectList(qw);
        List invoiceTypeNameList = new LinkedList();
        for(int i=0;i<rlist.size();i++){
            invoiceTypeNameList.add(rlist.get(i).getInvoicetypeName());
        }
        if(invoiceTypeNameList.contains(invoicetypeName) == true){
            errorStr += "发票类型已存在；";
        }

        Map lmp = new LinkedHashMap();
        if(errorStr != ""){
            lmp.put("code",0);
            lmp.put("info","faid");
            lmp.put("data",errorStr);
        }
        else {
            int r = systemInvoiceTypeMapper.insert(systemInvoiceTypeEntity);
            if(r != 1){
                lmp.put("code",0);
                lmp.put("info","faid");
                lmp.put("data","插入失败；");
            }
            else {
                lmp.put("code",1);
                lmp.put("info","success");
            }
        }
        return (LinkedHashMap) lmp;
    }
}
