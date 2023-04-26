package com.mycom.service.impl.invoice;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.InvoiceInvoiceEntity;
import com.mycom.mapper.*;
import com.mycom.service.invoice.OneInvoiceService;
import lombok.Data;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.LinkedHashMap;
import java.util.Map;

@Service
public class OneInvoiceImpl extends ServiceImpl<InvoiceInvoiceMapper, InvoiceInvoiceEntity> implements OneInvoiceService {
    @Autowired
    InvoiceInvoiceMapper invoiceInvoiceMapper;
    @Autowired
    SystemCompanyMapper systemCompanyMapper;
    @Autowired
    SystemDepartmentMapper systemDepartmentMapper;
    @Autowired
    SystemProductMapper systemProductMapper;
    @Autowired
    SystemUserMapper systemUserMapper;
    @Autowired
    SystemInvoiceTypeMapper systemInvoiceTypeMapper;

    @Override
    public LinkedHashMap GetOneInvoice(Integer invoiceId){
        Map lmp0 = new LinkedHashMap();
        InvoiceInvoiceEntity invoiceInvoiceEntity = invoiceInvoiceMapper.selectById(invoiceId);

        Integer companyId = invoiceInvoiceEntity.getCompany_id();
        String companyName = systemCompanyMapper.selectById(companyId).getCompany_name();
        lmp0.put("company_name",companyName);

        Integer departmentId = invoiceInvoiceEntity.getDepartment_id();
        String DepartmentName = systemDepartmentMapper.selectById(departmentId).getDepartment_name();
        lmp0.put("department_name",DepartmentName);

        Integer productId = invoiceInvoiceEntity.getProduct_id();
        String productName = systemProductMapper.selectById(productId).getProduct_name();
        lmp0.put("product_name",productName);

        Integer userId = invoiceInvoiceEntity.getUser_id();
        String userName = systemUserMapper.selectById(userId).getUser_name();
        lmp0.put("user_name",userName);

        Integer invoicetypeId = invoiceInvoiceEntity.getInvoicetype_id();
        String invoicetypeName = systemInvoiceTypeMapper.selectById(invoicetypeId).getInvoicetypeName();
        lmp0.put("invoicetype_name",invoicetypeName);

        Integer invoiceAmount = invoiceInvoiceEntity.getInvoice_amount();
        String invoiceCode = invoiceInvoiceEntity.getInvoice_code();
        String invoiceExplain = invoiceInvoiceEntity.getInvoice_explain();
        Date creatTime = invoiceInvoiceEntity.getCreat_time();

        Map lmp = new LinkedHashMap();
        lmp.put("code",1);
        lmp.put("info","success");
        lmp.put("data",lmp0);

        return (LinkedHashMap) lmp;
    }
}
