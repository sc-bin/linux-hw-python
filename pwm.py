
control_path = {
    0: "/sys/class/pwm/pwmchip0",
    1: "/sys/class/pwm/pwmchip16",
    2: "/sys/class/pwm/pwmchip20",
    3: "/sys/class/pwm/pwmchip22",
}

def write_to_file(path: str, value: str) -> None:
    with open(path, "w") as f:
        f.write(value)

def pwm_export(control: int, channel: int) -> None:
    """导出PWM通道
    @param control 控制器编号0 1 2 3
    @param channel PWM通道号
    """
    write_to_file(f"{control_path[control]}/export", str(channel))

def pwm_config(control: int, channel: int, period: int, duty_cycle: int) -> None:
    """配置PWM通道的参数。
    @param control 控制器编号0 1 2 3
    @param channel PWM通道号
    @param period PWM信号的周期，单位为纳秒。
    @param duty_cycle PWM信号的高电平时长。
    """
    write_to_file(f"{control_path[control]}/pwm{channel}/period", str(period))
    write_to_file(f"{control_path[control]}/pwm{channel}/duty_cycle", str(duty_cycle))
    write_to_file(f"{control_path[control]}/pwm{channel}/polarity", "normal")

def pwm_enable(control: int, channel: int) -> None:
    """启用PWM通道的输出。
    @param control 控制器编号0 1 2 3
    @param channel PWM通道号
    """
    write_to_file(f"{control_path[control]}/pwm{channel}/enable", "1")

def pwm_disable(control: int, channel: int) -> None:
    """关闭PWM通道的输出。
    @param control 控制器编号0 1 2 3
    @param channel PWM通道号
    """
    write_to_file(f"{control_path[control]}/pwm{channel}/enable", "0")

pwm_export(1, 0)  # 导出PWM通道
pwm_config(1, 0, 100000, 50000)  # 配置PWM周期和占空比
pwm_enable(1, 0)  # 启用PWM输出
