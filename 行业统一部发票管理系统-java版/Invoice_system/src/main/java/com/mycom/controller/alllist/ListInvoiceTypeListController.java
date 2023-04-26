package com.mycom.controller.alllist;

import com.mycom.service.alllist.ListInvoiceTypeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class ListInvoiceTypeListController {
    @Autowired
    ListInvoiceTypeService listInvoiceTypeService;

    @GetMapping("/get_invoicetype_list")
    @ResponseBody
    public Object GetInvoiceTypeList(){
        return listInvoiceTypeService.GetInvoiceTypeList();
    }
}
//http://127.0.0.1:5003/get_invoicetype_list