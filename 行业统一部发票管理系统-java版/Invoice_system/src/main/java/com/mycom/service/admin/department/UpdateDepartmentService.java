package com.mycom.service.admin.department;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.entity.SystemDepartmentEntity;

import java.util.LinkedHashMap;

public interface UpdateDepartmentService extends IService<SystemDepartmentEntity> {
    public LinkedHashMap updateDepartment(SystemDepartmentEntity systemDepartmentEntity);
}
