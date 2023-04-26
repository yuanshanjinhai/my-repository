package com.mycom.controller.admin.invoicetype;

import com.mycom.entity.SystemInvoiceTypeEntity;
import com.mycom.service.admin.invoicetype.UpdateInvoicetypeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.LinkedHashMap;

@RestController
public class UpdateInvoicetypeController {
    @Autowired
    UpdateInvoicetypeService updateInvoicetypeService;

    @GetMapping("/update_invoicetype")
    public LinkedHashMap UpdateInvoicetype(SystemInvoiceTypeEntity systemInvoiceTypeEntity){
        return updateInvoicetypeService.UpdateInvoicetype(systemInvoiceTypeEntity);
    }
}
// http://127.0.0.1:5003/update_invoicetype?id=7&invoicetypeName=搓澡