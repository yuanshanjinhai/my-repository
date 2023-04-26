package com.mycom.controller.invoice;

import com.mycom.service.invoice.OneInvoiceService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.LinkedHashMap;

@RestController
public class OneInvoiceController {
    @Autowired
    OneInvoiceService oneInvoiceService;

    @GetMapping("one_invoice")
    public LinkedHashMap GetOneInvoice(Integer invoiceId){
        return oneInvoiceService.GetOneInvoice(invoiceId);
    }
}
// http://127.0.0.1:5003/one_invoice?invoiceId=1