package com.mycom.controller.invoice;

import com.mycom.service.invoice.AllInvoiceService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.LinkedHashMap;

@RestController
public class AllInvoiceController {
    @Autowired
    AllInvoiceService allInvoiceService;

    @GetMapping("/all_invoice")
    public LinkedHashMap GetAllInvoice(Integer companyId,Integer departmentId,Integer productId,Integer userId){
        return allInvoiceService.GetAllInvoice(companyId,departmentId,productId,userId);
    }
}
// http://127.0.0.1:5003/all_invoice