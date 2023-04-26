package com.mycom.controller.admin.product;

import com.mycom.service.admin.product.OneProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.LinkedHashMap;

@RestController
public class OneProductController {
    @Autowired
    OneProductService oneProductService;

    @GetMapping("/one_prodect")
    public LinkedHashMap GetOneProduct(@RequestParam Integer productId){
        return oneProductService.GetOneProduct(productId);
    }
}
// http://127.0.0.1:5003/one_prodect?productId=3