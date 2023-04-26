package com.mycom.service.admin.department;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.entity.SystemDepartmentEntity;
import com.mycom.model.SystemDepartmentCompanyVO;

import java.util.LinkedHashMap;

public interface InsertDepartmenService extends IService<SystemDepartmentCompanyVO> {
    LinkedHashMap insertDepartment(SystemDepartmentCompanyVO systemDepartmentCompanyVO);
}
