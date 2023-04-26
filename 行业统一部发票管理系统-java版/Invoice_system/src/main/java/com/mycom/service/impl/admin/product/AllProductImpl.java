package com.mycom.service.impl.admin.product;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.SystemProductEntity;
import com.mycom.mapper.SystemProductMapper;
import com.mycom.service.admin.product.AllProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

@Service
public class AllProductImpl extends ServiceImpl<SystemProductMapper, SystemProductEntity> implements AllProductService {
    @Autowired
    SystemProductMapper systemProductMapper;

    @Override
    public LinkedHashMap GetAllProduct(String productName){
        QueryWrapper<SystemProductEntity> qw = new QueryWrapper<>();
        List<SystemProductEntity> rlist0;
        List rlist = new ArrayList();
        Map lmp = new LinkedHashMap();

        if (productName == null){
            rlist0 = systemProductMapper.selectList(qw);
        }
        else {
            qw.select().like("product_name",productName);
            rlist0 = systemProductMapper.selectList(qw);
        }

        if(rlist0.isEmpty() == false){
            for(int i=0;i<rlist0.size();i++){
                Map lmp0 = new LinkedHashMap();
                lmp0.put("id",rlist0.get(i).getId());
                lmp0.put("product_name",rlist0.get(i).getProduct_name());
                lmp0.put("product_abbreviation",rlist0.get(i).getProduct_abbreviation());
                lmp0.put("product_explain",rlist0.get(i).getProduct_explain());
                rlist.add(lmp0);
            }
        }
        lmp.put("code",1);
        lmp.put("info","success");
        lmp.put("data",rlist);
        return (LinkedHashMap) lmp;

    }
}
