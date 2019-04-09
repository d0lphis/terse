################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/client_process.c \
../src/common.c \
../src/ftpserver.c \
../src/serv_client.c 

OBJS += \
./src/client_process.o \
./src/common.o \
./src/ftpserver.o \
./src/serv_client.o 

C_DEPS += \
./src/client_process.d \
./src/common.d \
./src/ftpserver.d \
./src/serv_client.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Cross GCC Compiler'
	gcc -O3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


