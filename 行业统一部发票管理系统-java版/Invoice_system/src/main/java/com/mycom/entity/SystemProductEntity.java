package com.mycom.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.util.Date;

@Data
@TableName("system_product")
public class SystemProductEntity {
    @TableId(value = "id",type = IdType.AUTO)
    private Integer id;
    private String product_name;
    private String product_abbreviation;
    private String product_explain;
    private Date creat_time;
}
