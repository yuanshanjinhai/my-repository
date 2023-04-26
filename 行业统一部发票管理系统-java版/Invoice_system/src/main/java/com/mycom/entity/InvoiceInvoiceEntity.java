package com.mycom.entity;

import com.baomidou.mybatisplus.annotation.*;
import lombok.Data;

import java.util.Date;

@Data
@TableName("invoice_invoice")
public class InvoiceInvoiceEntity {
    @TableId(value = "id",type = IdType.AUTO)
    private Integer id;
    private Integer user_id;
    private Integer company_id;
    private Integer department_id;
    private Integer product_id;
    private Integer invoicetype_id;
    private Integer invoice_amount;
    private String invoice_code;
    private String invoice_explain;
    private Date creat_time;
}
