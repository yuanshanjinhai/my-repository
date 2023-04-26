package com.mycom.service.impl.admin.department;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.SystemDepartmentEntity;
import com.mycom.mapper.SystemDepartmentMapper;
import com.mycom.service.admin.department.UpdateDepartmentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.LinkedHashMap;
import java.util.Map;

@Service
public class UpdateDepartmentImpl extends ServiceImpl<SystemDepartmentMapper, SystemDepartmentEntity> implements UpdateDepartmentService {

    @Autowired
    SystemDepartmentMapper systemDepartmentMapper;

    @Override
    public LinkedHashMap updateDepartment(SystemDepartmentEntity systemDepartmentEntity){
        Integer departmentId = systemDepartmentEntity.getId();
        String departmentName = systemDepartmentEntity.getDepartment_name();
        String departmentExplain = systemDepartmentEntity.getDepartment_explain();
        Map lmp = new LinkedHashMap();

        String errorStr = "";
        if(departmentName == null){
            errorStr += "部门名称不能为空；";
        }
        else {
            if(departmentName.length() > 30){
                errorStr += "部门名称不能超过30个字；";
            }
        }
        if(departmentExplain.length() > 1000){
            errorStr += "部门说明不能超过1000个字";
        }

        if(errorStr == ""){
            int r = systemDepartmentMapper.updateById(systemDepartmentEntity);
            if(r == 0){
                lmp.put("code",0);
                lmp.put("info","faid");
                lmp.put("data","更新失败；");
            }
            else {
                lmp.put("code",1);
                lmp.put("info","success");
            }
        }
        else {
            lmp.put("code",0);
            lmp.put("info","faid");
            lmp.put("data",errorStr);
        }
        return (LinkedHashMap) lmp;
    }
}
