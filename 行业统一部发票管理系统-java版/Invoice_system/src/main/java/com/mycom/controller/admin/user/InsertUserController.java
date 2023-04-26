package com.mycom.controller.admin.user;

import com.mycom.entity.SystemUserEntity;
import com.mycom.service.admin.user.InsertUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.LinkedHashMap;

@RestController
public class InsertUserController {
    @Autowired
    InsertUserService snsertUserService;

    @PostMapping("/insert_user")
    public LinkedHashMap InserUser(@RequestBody SystemUserEntity systemUserEntity){
        return snsertUserService.InsertUser(systemUserEntity);
    }
}
// http://127.0.0.1:5003/insert_user
// {"user_login_name":"zhaojinghu","user_name":"赵静湖","password":"123456","company_id":3,"department_id":2}