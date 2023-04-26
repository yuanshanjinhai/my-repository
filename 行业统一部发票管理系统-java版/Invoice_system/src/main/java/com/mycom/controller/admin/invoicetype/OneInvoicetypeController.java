package com.mycom.controller.admin.invoicetype;

import com.mycom.entity.SystemInvoiceTypeEntity;
import com.mycom.service.admin.invoicetype.OneInvoicetypeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.LinkedHashMap;

@RestController
public class OneInvoicetypeController {
    @Autowired
    OneInvoicetypeService oneInvoicetypeService;

    @GetMapping("/one_invoicetype")
    public LinkedHashMap GetOneInvoicetype(@RequestParam Integer invoicetypeId){
        return oneInvoicetypeService.GetOneInvoicetype(invoicetypeId);
    }
}
// http://127.0.0.1:5003/one_invoicetype?invoicetypeId=7