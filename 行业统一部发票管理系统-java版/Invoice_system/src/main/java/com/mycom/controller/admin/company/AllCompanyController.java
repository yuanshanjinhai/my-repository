package com.mycom.controller.admin.company;

import com.mycom.service.admin.company.AllCompanyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class AllCompanyController {
    @Autowired
    AllCompanyService allCompanyService;

    @GetMapping("/get_all_company")
    @ResponseBody
    public Object GetCompanyList(@RequestParam (value = "companyName",required=false) String companyName){
        return allCompanyService.GetAllCompany(companyName);
    }
}
//http://127.0.0.1:5003/get_all_company