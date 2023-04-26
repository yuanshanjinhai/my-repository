package com.mycom.service.impl.admin.department;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.SystemDepartmentEntity;
import com.mycom.mapper.SystemDepartmentMapper;
import com.mycom.service.admin.department.OneDepartrmentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.LinkedHashMap;
import java.util.Map;

@Service
public class OneDepatrmentImpl extends ServiceImpl<SystemDepartmentMapper, SystemDepartmentEntity> implements OneDepartrmentService {
    @Autowired
    SystemDepartmentMapper systemDepartmentMapper;

    @Override
    public LinkedHashMap GetOneDepartment(Integer DepartmentId){
        QueryWrapper<SystemDepartmentEntity> qw = new QueryWrapper<>();
        SystemDepartmentEntity sec = systemDepartmentMapper.selectById(DepartmentId);

        Map lmp0 = new LinkedHashMap();
        lmp0.put("id",sec.getId());
        lmp0.put("department_name",sec.getDepartment_name());
        lmp0.put("department_explain",sec.getDepartment_explain());

        Map lmp = new LinkedHashMap();
        lmp.put("code",1);
        lmp.put("info","success");
        lmp.put("data",lmp0);

        return (LinkedHashMap) lmp;
    }
}
