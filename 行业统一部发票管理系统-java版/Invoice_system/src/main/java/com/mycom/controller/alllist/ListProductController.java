package com.mycom.controller.alllist;

import com.mycom.service.alllist.ListProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ListProductController {
    @Autowired
    ListProductService systemProductService;

    @GetMapping("/get_prodect_list")
    @ResponseBody
    public Object GetUserListr() {
        return systemProductService.GetProductList();
    }
}
//http://127.0.0.1:5003/get_prodect_list