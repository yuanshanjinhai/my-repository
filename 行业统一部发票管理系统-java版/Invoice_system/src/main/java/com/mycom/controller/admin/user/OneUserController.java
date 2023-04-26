package com.mycom.controller.admin.user;

import com.mycom.service.admin.user.OneUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.LinkedHashMap;

@RestController
public class OneUserController {
    @Autowired
    OneUserService oneUserService;

    @GetMapping("/one_user")
    public LinkedHashMap GetOneUser(@RequestParam Integer userId){

        return oneUserService.OneUser(userId);
    }
}
// http://127.0.0.1:5003/one_user?userId=1