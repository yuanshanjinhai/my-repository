package com.mycom.service.impl.invoice;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.InvoiceInvoiceEntity;
import com.mycom.mapper.*;
import com.mycom.service.invoice.StatisticAlanalysisService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class StatisticAlanalysisImpl extends ServiceImpl<InvoiceInvoiceMapper, InvoiceInvoiceEntity> implements StatisticAlanalysisService {
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

    public LinkedHashMap statisticAlanalysis(Integer companyId, Integer departmentId, Integer productId, Integer userId, Date startTime, Date endTime) {
        QueryWrapper<InvoiceInvoiceEntity> qw = new QueryWrapper<>();
        List<InvoiceInvoiceEntity> rlist0 = null;
        // 000000
        if (companyId == null && departmentId == null && productId == null && userId == null && startTime == null && endTime == null) {
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 100000
        if (companyId != null && departmentId == null && productId == null && userId == null && startTime == null && endTime == null) {
            qw.select().eq("company_id", companyId);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 001000
        if (companyId == null && departmentId == null && productId != null && userId == null && startTime == null && endTime == null) {
            qw.select().eq("product_id", productId);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 000100
        if (companyId == null && departmentId == null && productId == null && userId != null && startTime == null && endTime == null) {
            System.out.println("11111111111111111111");
            qw.select().eq("user_id", userId.toString());
            rlist0 = invoiceInvoiceMapper.selectList(qw);
            System.out.println("rlist00=" +rlist0);
        }
        // 000010
        if (companyId == null && departmentId == null && productId == null && userId == null && startTime != null && endTime == null) {
            qw.select().gt("creat_time", startTime);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 000001
        if (companyId == null && departmentId == null && productId == null && userId == null && startTime == null && endTime != null) {
            qw.select().lt("creat_time", endTime);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 110000
        if (companyId != null && departmentId != null && productId == null && userId != null && startTime == null && endTime == null) {
            qw.select().eq("company_id", companyId).eq("department_id", departmentId);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 001100
        if (companyId == null && departmentId == null && productId != null && userId != null && startTime == null && endTime == null) {
            qw.select().eq("product_id", productId).eq("user_id", userId);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 000110
        if (companyId == null && departmentId == null && productId == null && userId != null && startTime != null && endTime == null) {
            qw.select().eq("user_id", userId).gt("creat_time",startTime);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 000011
        if (companyId == null && departmentId == null && productId == null && userId == null && startTime != null && endTime != null) {
            qw.select().gt("creat_time",startTime).lt("creat_time",endTime);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 111000
        if (companyId != null && departmentId != null && productId != null && userId == null && startTime == null && endTime == null) {
            qw.select().eq("company_id", companyId).eq("department_id", departmentId).eq("product_id", productId);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 001110
        if (companyId == null && departmentId == null && productId != null && userId != null && startTime != null && endTime == null) {
            qw.select().eq("product_id", productId).eq("user_id", userId).gt("creat_time", startTime);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 000111
        if (companyId == null && departmentId == null && productId == null && userId != null && startTime != null && endTime != null) {
            qw.select().eq("user_id", userId).gt("creat_time", startTime).lt("creat_time",endTime);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 111100
        if (companyId != null && departmentId != null && productId != null && userId != null && startTime == null && endTime == null) {
            qw.select().eq("company_id", companyId).eq("department_id", departmentId).eq("product_id", productId).eq("user_id", userId);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 011110
        if (companyId == null && departmentId != null && productId != null && userId != null && startTime != null && endTime == null) {
            qw.select().eq("department_id", departmentId).eq("product_id", productId).eq("user_id", userId).gt("creat_time",startTime);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }
        // 001111
        if (companyId == null && departmentId == null && productId != null && userId == null && startTime != null && endTime != null) {
            qw.select().eq("product_id", productId).eq("user_id", userId).gt("creat_time",startTime).lt("creat_time",endTime);
            rlist0 = invoiceInvoiceMapper.selectList(qw);
        }

        System.out.println("rlist0=" +rlist0);
        List rlist = new ArrayList();
        for (int i = 0; i < rlist0.size(); i++) {
            Map lmp0 = new LinkedHashMap();

            Integer rcompanyId = rlist0.get(i).getCompany_id();
            String companyName = systemCompanyMapper.selectById(rcompanyId).getCompany_name();
            lmp0.put("company_name", companyName);

            Integer rDepartmentId = rlist0.get(i).getDepartment_id();
            String DepartmentName = systemDepartmentMapper.selectById(rDepartmentId).getDepartment_name();
            lmp0.put("department_name", DepartmentName);

            Integer rProductId = rlist0.get(i).getProduct_id();
            String productName = systemProductMapper.selectById(rProductId).getProduct_name();
            lmp0.put("product_name", productName);

            Integer rUserId = rlist0.get(i).getUser_id();
            String userName = systemUserMapper.selectById(rUserId).getUser_name();
            lmp0.put("user_name", userName);

            Integer invoicetypeId = rlist0.get(i).getInvoicetype_id();
            String invoicetypeName = systemInvoiceTypeMapper.selectById(invoicetypeId).getInvoicetypeName();
            lmp0.put("invoicetype_name", invoicetypeName);

            lmp0.put("invoice_amount", rlist0.get(i).getInvoice_amount());
            lmp0.put("invoice_code", rlist0.get(i).getInvoice_code());
            lmp0.put("invoice_explain", rlist0.get(i).getInvoice_explain());
            lmp0.put("creat_time", rlist0.get(i).getCreat_time());

            rlist.add(lmp0);
        }
        Map lmp = new LinkedHashMap();
        lmp.put("code", 1);
        lmp.put("info", "success");
        lmp.put("data", rlist);
        return (LinkedHashMap) lmp;
    }
}
