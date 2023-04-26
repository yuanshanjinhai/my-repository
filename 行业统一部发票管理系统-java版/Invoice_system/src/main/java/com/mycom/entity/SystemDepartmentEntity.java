package com.mycom.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@Data
@TableName("system_department")
public class SystemDepartmentEntity {
    @TableId(value = "id",type = IdType.AUTO)
    private Integer id;
    private String department_name;
    private String department_explain;
}
