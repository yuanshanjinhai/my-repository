package com.mycom.controller.admin.user;

import com.mycom.entity.SystemUserEntity;
import com.mycom.service.admin.user.UpdateUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.LinkedHashMap;

@RestController
public class UpdateUserController {
    @Autowired
    UpdateUserService updateUserService;

    @PostMapping("/update_user")
    public LinkedHashMap UpdateUser(@RequestBody SystemUserEntity systemUserEntity){
        return updateUserService.UpdateUser(systemUserEntity);
    }
}
// http://127.0.0.1:5003/update_user
// {"id":4,"user_login_name":"zhaojinghu1","user_name":"赵静湖","password":"123456","company_id":3,"department_id":1}