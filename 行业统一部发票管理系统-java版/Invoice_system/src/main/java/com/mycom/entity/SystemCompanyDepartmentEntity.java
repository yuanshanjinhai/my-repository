package com.mycom.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@Data
@TableName("system_company_department")
public class SystemCompanyDepartmentEntity {
    @TableId(value = "id",type = IdType.AUTO)
    private Integer id;
    private Integer company_id;
    private Integer department_id;
}
