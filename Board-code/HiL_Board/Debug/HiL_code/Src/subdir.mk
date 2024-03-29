################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (10.3-2021.10)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../HiL_code/Src/HiL_MSGQ.c \
../HiL_code/Src/HiL_callbacks.c \
../HiL_code/Src/HiL_controller.c \
../HiL_code/Src/HiL_gateway.c \
../HiL_code/Src/HiL_mcu_commands.c 

OBJS += \
./HiL_code/Src/HiL_MSGQ.o \
./HiL_code/Src/HiL_callbacks.o \
./HiL_code/Src/HiL_controller.o \
./HiL_code/Src/HiL_gateway.o \
./HiL_code/Src/HiL_mcu_commands.o 

C_DEPS += \
./HiL_code/Src/HiL_MSGQ.d \
./HiL_code/Src/HiL_callbacks.d \
./HiL_code/Src/HiL_controller.d \
./HiL_code/Src/HiL_gateway.d \
./HiL_code/Src/HiL_mcu_commands.d 


# Each subdirectory must supply rules for building sources it contributes
HiL_code/Src/%.o HiL_code/Src/%.su: ../HiL_code/Src/%.c HiL_code/Src/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m7 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F767xx -c -I../Core/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F7xx/Include -I../Drivers/CMSIS/Include -I../USB_DEVICE/App -I../USB_DEVICE/Target -I../Middlewares/Third_Party/FreeRTOS/Source/include -I../Middlewares/Third_Party/FreeRTOS/Source/CMSIS_RTOS_V2 -I../Middlewares/Third_Party/FreeRTOS/Source/portable/GCC/ARM_CM7/r0p1 -I../Middlewares/ST/STM32_USB_Device_Library/Core/Inc -I../Middlewares/ST/STM32_USB_Device_Library/Class/CDC/Inc -I"C:/SKOLAN H/T11/Embedded Projekt IL2232/Github/SOFTWARE_DEV/Board-code/HiL_Board/HiL_code" -I"C:/SKOLAN H/T11/Embedded Projekt IL2232/Github/SOFTWARE_DEV/Board-code/HiL_Board/HiL_code/Inc" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv5-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-HiL_code-2f-Src

clean-HiL_code-2f-Src:
	-$(RM) ./HiL_code/Src/HiL_MSGQ.d ./HiL_code/Src/HiL_MSGQ.o ./HiL_code/Src/HiL_MSGQ.su ./HiL_code/Src/HiL_callbacks.d ./HiL_code/Src/HiL_callbacks.o ./HiL_code/Src/HiL_callbacks.su ./HiL_code/Src/HiL_controller.d ./HiL_code/Src/HiL_controller.o ./HiL_code/Src/HiL_controller.su ./HiL_code/Src/HiL_gateway.d ./HiL_code/Src/HiL_gateway.o ./HiL_code/Src/HiL_gateway.su ./HiL_code/Src/HiL_mcu_commands.d ./HiL_code/Src/HiL_mcu_commands.o ./HiL_code/Src/HiL_mcu_commands.su

.PHONY: clean-HiL_code-2f-Src

