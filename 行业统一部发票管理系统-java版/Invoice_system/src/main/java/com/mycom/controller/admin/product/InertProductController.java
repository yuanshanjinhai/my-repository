package com.mycom.controller.admin.product;

import com.mycom.entity.SystemProductEntity;
import com.mycom.service.admin.product.InsertProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.LinkedHashMap;

@RestController
public class InertProductController {
    @Autowired
    InsertProductService insertProductService;

    @PostMapping("/insert_product")
    public LinkedHashMap InsertProduct(@RequestBody SystemProductEntity systemProductEntity){
        return insertProductService.InsertProduct(systemProductEntity);
    }
}
// http://127.0.0.1:5003/insert_product
// {"product_name":"罪犯管理系统","product_abbreviation":"XF_system","product_explain":"管理罪犯之用"}