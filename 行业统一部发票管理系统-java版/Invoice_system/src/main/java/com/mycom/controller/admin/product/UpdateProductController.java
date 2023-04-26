package com.mycom.controller.admin.product;

import com.mycom.entity.SystemProductEntity;
import com.mycom.service.admin.product.UpdateProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.LinkedHashMap;

@RestController
public class UpdateProductController {
    @Autowired
    UpdateProductService updateProductService;

    @PostMapping("/update_product")
    public LinkedHashMap UpdateProduct(@RequestBody SystemProductEntity systemProductEntity){
        return updateProductService.UpdateProdect(systemProductEntity);
    }
}
// http://127.0.0.1:5003/update_product
// {"id":4,"product_name":"罪犯管理系统","product_abbreviation":"XF_system","product_explain":"管理罪犯之用"}