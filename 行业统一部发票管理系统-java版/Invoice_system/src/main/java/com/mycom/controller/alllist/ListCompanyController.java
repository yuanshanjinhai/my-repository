package com.mycom.controller.alllist;

import com.mycom.service.alllist.ListCompanyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class ListCompanyController {
    @Autowired
    ListCompanyService listCompanyService;

    @GetMapping("/get_company_list")
    @ResponseBody
    public Object GetCompanyList(){

        return listCompanyService.GetCompanyList();
    }
}
//http://127.0.0.1:5003/get_company_list