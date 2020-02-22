## This Python script runs automated TRNSYS simulation
#   prepared by Hakan İbrahim Tol, PhD at TU/e on 22/02/2020
#   thanks to Len Rijvers, PDEng

#  Libraries Imported
import subprocess           # to run the TRNSYS simulation
import shutil               # to duplicate the output txt file
import time                 # to measure the computation time

# List of Parameters to be Evaluated
list_t_on  =[7,8,9]         # [hour] Time when high-operation is on
list_t_off =[21,22,23]      # [hour] Time when high-operation is off
list_s_high =[0.8,0.9,1]    # [-] High control signal
list_s_low =[0.1,0.3,0.5]   # [-] Low control signal

label_no=0

#  Looping through Each of Combinations (List of Parameters)
for s_high in list_s_high:
    for s_low in list_s_low:
        for t_on in list_t_on:
            for t_off in list_t_off:
            
                # 1) Assigning parameter values as input in the TRNSYS (.dck) file

                #  - opening dublicated template .dck file (parameter values changed to pyt tags via NotePad for the first time i.e. pyt_t_on in this template z_pyt_TEMPLATE.dck)
                with open('z_pyt_TEMPLATE.dck', 'r') as file_in:
                    filedata = file_in.read()
                    
                #  - changing/replacing the pyt tags to parameter values in the .dck text
                filedata = filedata.replace('pyt_t_on', str(t_on))
                filedata = filedata.replace('pyt_t_off', str(t_off))
                filedata = filedata.replace('pyt_s_high', str(s_high))
                filedata = filedata.replace('pyt_s_low', str(s_low))

                #  - (over)writing the modified template .dck file to the original .dck file (to be run by TRNSYS) 
                with open('ExampleTRNSYSmodel.dck', 'w') as dckfile_out:
                    dckfile_out.write(filedata)

                # 2) Running TRNSYS simulation
                start_time=time.time()                  # Measuring time (start point)
                subprocess.run([r"C:\Trnsys17\Exe\TRNExe.exe",r"C:\zGithub\ExampleTRNSYSmodel.dck","/h"])
                elapsed_time = time.time() - start_time # Measuring time (end point)
                print(elapsed_time)

                # 3) Generating the output .txt file name for each of the simulation results (i.e. first one as 001.txt)
                label_no+=1
                t=str(label_no)
                filename_out=t.rjust(3, '0')+'.txt'

                shutil.copy('trnOut_PumpData.txt', filename_out)
