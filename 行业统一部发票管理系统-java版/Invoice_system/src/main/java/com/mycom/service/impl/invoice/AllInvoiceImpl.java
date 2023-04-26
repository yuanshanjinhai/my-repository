package com.mycom.service.impl.invoice;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.InvoiceInvoiceEntity;
import com.mycom.mapper.*;
import com.mycom.service.invoice.AllInvoiceService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

@Service
public class AllInvoiceImpl extends ServiceImpl<InvoiceInvoiceMapper, InvoiceInvoiceEntity> implements AllInvoiceService {
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

    public LinkedHashMap GetAllInvoice(Integer companyId, Integer departmentId, Integer productId, Integer userId){
        QueryWrapper<InvoiceInvoiceEntity> qw = new QueryWrapper<>();
        List<InvoiceInvoiceEntity> rlist0 = null;
        // 0000
        if(companyId == null && departmentId == null && productId == null && userId == null){
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 1000
        if(companyId != null && departmentId == null && productId == null && userId == null){
            qw.select().eq("company_id",companyId);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 0010
        if(companyId == null && departmentId == null && productId != null && userId == null){
            qw.select().eq("product_id",productId);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 0001
        if(companyId == null && departmentId == null && productId == null && userId != null){
            qw.select().eq("user_id",userId.toString());
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 1100
        if(companyId == null && departmentId == null && productId == null && userId != null){
            qw.select().eq("company_id",companyId).eq("department_id",departmentId);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 0011
        if(companyId == null && departmentId == null && productId == null && userId != null){
            qw.select().eq("product_id",productId).eq("user_id",userId);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 1110
        if(companyId == null && departmentId == null && productId == null && userId != null){
            qw.select().eq("company_id",companyId).eq("department_id",departmentId).eq("product_id",productId);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 1111
        if(companyId == null && departmentId == null && productId == null && userId != null){
            qw.select().eq("company_id",companyId).eq("department_id",departmentId).eq("product_id",productId).eq("user_id",userId);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }

        List rlist = new ArrayList();
        for(int i=0;i<rlist0.size();i++){
            Map lmp0 = new LinkedHashMap();

            Integer rcompanyId = rlist0.get(i).getCompany_id();
            String companyName = systemCompanyMapper.selectById(rcompanyId).getCompany_name();
            lmp0.put("company_name",companyName);

            Integer rDepartmentId = rlist0.get(i).getDepartment_id();
            String DepartmentName = systemDepartmentMapper.selectById(rDepartmentId).getDepartment_name();
            lmp0.put("department_name",DepartmentName);

            Integer rProductId = rlist0.get(i).getProduct_id();
            String productName = systemProductMapper.selectById(rProductId).getProduct_name();
            lmp0.put("product_name",productName);

            Integer rUserId = rlist0.get(i).getUser_id();
            String userName = systemUserMapper.selectById(rUserId).getUser_name();
            lmp0.put("user_name",userName);

            Integer invoicetypeId = rlist0.get(i).getInvoicetype_id();
            String invoicetypeName = systemInvoiceTypeMapper.selectById(invoicetypeId).getInvoicetypeName();
            lmp0.put("invoicetype_name",invoicetypeName);

            lmp0.put("invoice_amount",rlist0.get(i).getInvoice_amount());
            lmp0.put("invoice_code",rlist0.get(i).getInvoice_code());
            lmp0.put("invoice_explain",rlist0.get(i).getInvoice_explain());
            lmp0.put("creat_time",rlist0.get(i).getCreat_time());

            rlist.add(lmp0);
        }
        Map lmp = new LinkedHashMap();
        lmp.put("code",1);
        lmp.put("info","success");
        lmp.put("data",rlist);
        return (LinkedHashMap) lmp;
    }
}
