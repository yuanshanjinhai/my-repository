package com.mycom.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@Data
@TableName("system_invoicetype")
public class SystemInvoiceTypeEntity {
    @TableId(value = "id",type = IdType.AUTO)
    private Integer id;
    @TableField("invoicetype_name")
    private String invoicetypeName;
}
