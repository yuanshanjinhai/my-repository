package com.mycom.model;

import lombok.Data;

// 插入部门，需要用到公司id
@Data
public class SystemDepartmentCompanyVO {
    private String departmentName;
    private String departmentExplain;
    private Integer companyId;
}
