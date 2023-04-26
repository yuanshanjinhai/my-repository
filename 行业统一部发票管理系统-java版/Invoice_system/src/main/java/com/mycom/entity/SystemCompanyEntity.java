package com.mycom.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.util.Date;

@Data
@TableName("system_company")
public class SystemCompanyEntity {
    @TableId(value = "id",type = IdType.AUTO)
    private Integer id;
    private String company_name;
    private String company_abbreviation;
    private String company_explain;
    private Date creat_time;
}
