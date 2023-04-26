package com.mycom.controller.admin.invoicetype;

import com.mycom.entity.SystemInvoiceTypeEntity;
import com.mycom.service.admin.invoicetype.InsertInvoicetypeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.LinkedHashMap;

@RestController
public class InsertInvoicetypeController {
    @Autowired
    InsertInvoicetypeService insertInvoicetypeService;

    @PostMapping("/insert_invoicetype")
    public LinkedHashMap InsertInvoicetype(@RequestBody SystemInvoiceTypeEntity systemInvoiceTypeEntity){
        return insertInvoicetypeService.InsertInvoicetype(systemInvoiceTypeEntity);
    }
}
// http://127.0.0.1:5003/insert_invoicetype
// {"invoicetypeName":"按摩"}