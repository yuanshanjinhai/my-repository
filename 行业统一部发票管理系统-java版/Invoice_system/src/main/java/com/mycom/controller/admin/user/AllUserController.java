package com.mycom.controller.admin.user;

import com.mycom.service.admin.user.AllUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.LinkedHashMap;

@RestController
public class AllUserController {
    @Autowired
    AllUserService allUserService;

    @GetMapping("/all_user")
    public LinkedHashMap GetAlluser (Integer companyId, Integer departmentId){
        return allUserService.GetAllUser(companyId, departmentId);
    }
}
// http://127.0.0.1:5003/all_user