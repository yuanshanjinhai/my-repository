package com.mycom.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.mycom.entity.SystemDepartmentEntity;
import org.apache.ibatis.annotations.Select;

public interface SystemDepartmentMapper extends BaseMapper<SystemDepartmentEntity> {
    @Select("<script>SELECT id FROM system_department ORDER BY id DESC LIMIT 1</script>")
    int selectDepartmentNewest();
}
