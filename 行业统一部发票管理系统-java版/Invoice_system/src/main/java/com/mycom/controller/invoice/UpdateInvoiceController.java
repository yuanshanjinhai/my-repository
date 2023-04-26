package com.mycom.controller.invoice;

import com.mycom.entity.InvoiceInvoiceEntity;
import com.mycom.service.invoice.UpdateInvoiceService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.LinkedHashMap;

@RestController
public class UpdateInvoiceController {
    @Autowired
    UpdateInvoiceService updateInvoiceService;

    @PostMapping("/update_invoice")
    public LinkedHashMap UpdateInvoice(@RequestBody InvoiceInvoiceEntity invoiceInvoiceEntity){
        return updateInvoiceService.UpdateInvoice(invoiceInvoiceEntity);
    }
}
// http://127.0.0.1:5003/update_invoice
// {"id":10,"company_id":3,"department_id":2,"product_id":1,"user_id":1,"invoicetype_id":2,"invoice_amount":800,"invoice_code":"jt123457","invoice_explain":"每天每日的交通费"}