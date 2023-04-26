package com.mycom.service.impl.invoice;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.InvoiceInvoiceEntity;
import com.mycom.mapper.InvoiceInvoiceMapper;
import com.mycom.service.invoice.UpdateInvoiceService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.LinkedHashMap;
import java.util.Map;

@Service
public class UpdateInvoiceImpl extends ServiceImpl<InvoiceInvoiceMapper, InvoiceInvoiceEntity> implements UpdateInvoiceService {
    @Autowired
    InvoiceInvoiceMapper invoiceInvoiceMapper;

    public LinkedHashMap UpdateInvoice(InvoiceInvoiceEntity invoiceInvoiceEntity){
        Integer companyId = invoiceInvoiceEntity.getCompany_id();
        Integer departmentId = invoiceInvoiceEntity.getDepartment_id();
        Integer productId = invoiceInvoiceEntity.getProduct_id();
        Integer userId = invoiceInvoiceEntity.getUser_id();
        Integer invoicetypeId = invoiceInvoiceEntity.getInvoicetype_id();
        Integer invoiceAmount = invoiceInvoiceEntity.getInvoice_amount();
        String invoiceCode = invoiceInvoiceEntity.getInvoice_code();
        String invoiceExplain = invoiceInvoiceEntity.getInvoice_explain();

        String errorStr = "";
        if(companyId == null){
            errorStr += "公司不能为空；";
        }
        if(departmentId == null){
            errorStr += "部门不能为空；";
        }
        if(productId == null){
            errorStr += "项目不能为空；";
        }
        if(userId == null){
            errorStr += "用户不能为空；";
        }
        if(invoicetypeId == null){
            errorStr += "发票类型不能为空；";
        }
        if(invoiceAmount == null){
            errorStr += "报销金额不能为空；";
        }
        if(invoiceCode == null){
            errorStr += "发票id不能为空；";
        }
        if(invoiceCode.length() > 30){
            errorStr += "发票id不能超过30个字符；";
        }
        if(invoiceExplain != null && invoiceExplain.length()>1000){
            errorStr += "发票说明不能超过1000个字；";
        }

        Map lmp = new LinkedHashMap();
        if(errorStr != ""){
            lmp.put("code",0);
            lmp.put("info","faid");
            lmp.put("data",errorStr);
        }
        else {
            Integer r = invoiceInvoiceMapper.updateById(invoiceInvoiceEntity);
            System.out.println("r=" +r);
            if(r == 0){
                lmp.put("code",0);
                lmp.put("info","faid");
                lmp.put("data","更新失败；");
            }
            else {
                lmp.put("code",1);
                lmp.put("info","success");
            }
        }
        return (LinkedHashMap) lmp;
    }
}
