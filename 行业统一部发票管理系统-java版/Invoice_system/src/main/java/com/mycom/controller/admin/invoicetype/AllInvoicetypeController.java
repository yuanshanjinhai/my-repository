package com.mycom.controller.admin.invoicetype;

import com.mycom.entity.SystemInvoiceTypeEntity;
import com.mycom.service.admin.invoicetype.AllInvoicetypeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.LinkedHashMap;

@RestController
public class AllInvoicetypeController {
    @Autowired
    AllInvoicetypeService allInvoicetypeService;

    @GetMapping("/all_invoicetype")
    public LinkedHashMap GetAllInvoicetype(SystemInvoiceTypeEntity systemInvoiceTypeEntity){
        return allInvoicetypeService.GetAllInvoicetype(systemInvoiceTypeEntity);
    }
}
// http://127.0.0.1:5003/all_invoicetype