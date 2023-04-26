package com.mycom.controller.alllist;

import com.mycom.service.alllist.ListUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ListUserController {
    @Autowired
    ListUserService listUserService;

    @GetMapping("/get_user_list")
    @ResponseBody
    public Object GetUserListr() {

        return listUserService.GetUserList();
    }
}
//http://127.0.0.1:5003/get_user_list