package com.mycom.controller.admin.product;

import com.mycom.service.admin.product.AllProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.LinkedHashMap;

@RestController
public class AllProductController {

    @Autowired
    AllProductService allProductService;

    @GetMapping("all_prodect")
    public LinkedHashMap GetAllProduct(String prodectName){
        return allProductService.GetAllProduct(prodectName);
    }
}
// http://127.0.0.1:5003/all_prodect
// http://127.0.0.1:5003/all_prodect?prodectName=人