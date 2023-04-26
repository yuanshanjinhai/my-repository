package com.mycom.controller.admin.company;

import com.mycom.service.admin.company.OneCompanyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.LinkedHashMap;

@Controller
public class OneCompanyController {
    @Autowired
    OneCompanyService oneCompanyService;

    @GetMapping("/one_company")
    @ResponseBody
    public LinkedHashMap OneCompany(@RequestParam Integer companyId){
        return oneCompanyService.GetOneCompany(companyId);
    }
}
//http://127.0.0.1:5003/one_company?companyId=7