import random




# Expanded Quiz data with 50+ questions
questions = [
    {"question": "Which register is commonly used to store the return address in ARM (RISC) architecture?", "choices": [" LR", " R0", " PC"]},
    {"question": "In x86 architecture, what is the purpose of the EAX register?", "choices": [" Base pointer", " Accumulator", " Stack pointer"]},
    {"question": "What is the 64-bit equivalent of the EBX register in x64 architecture?", "choices": [" RBX", " RAX", " RCX"]},
    {"question": "Which register is typically used for counting in loops in x86 architecture?", "choices": [" EAX", " ECX", " ESI"]},
    {"question": "What register holds the instruction pointer in x64 architecture?", "choices": [" RIP", " RBP", " RDI"]},
    {"question": "Which register in ARM architecture is used as the Program Counter (PC)?", "choices": [" R14", " R15", " R13"]},
    {"question": "In older Intel architecture, what is the purpose of the BP register?", "choices": [" Stack pointer", " Accumulator", " Base pointer"]},
    {"question": "Which 32-bit Linux register is used to store the stack pointer?", "choices": [" ESP", " EBP", " ESI"]},
    {"question": "In 64-bit Linux, what is the purpose of the RAX register?", "choices": [" Accumulator", " Base pointer", " Stack pointer"]},
    {"question": "Which register is the Frame Pointer in x86 architecture?", "choices": [" ESI", " EBP", " ESP"]},
    {"question": "What register in ARM is used to store the stack pointer?", "choices": [" SP", " LR", " PC"]},
    {"question": "In x86 architecture, what register is used for the index source in string operations?", "choices": [" ESI", " EDI", " ECX"]},
    {"question": "Which register is the destination index in x86 architecture?", "choices": [" ESI", " EDI", " EBX"]},
    {"question": "In x64 architecture, what is the 64-bit equivalent of ESI?", "choices": [" RSI", " RDI", " RBP"]},
    {"question": "Which ARM register is used to hold the current stack frame?", "choices": [" FP", " PC", " SP"]},
    {"question": "In older Intel architecture, which register is used for multiplication and division?", "choices": [" AX", " BX", " DX"]},
    {"question": "What is the main register used for function return values in x86 architecture?", "choices": [" EBX", " EAX", " ECX"]},
    {"question": "In ARM architecture, which register is used to store the link register?", "choices": [" R14", " R12", " R11"]},
    {"question": "In 32-bit Linux systems, what register stores the base pointer?", "choices": [" ESP", " EBP", " ESI"]},
    {"question": "In ARM architecture, what is the role of the R13 register?", "choices": [" Stack pointer", " Program counter", " Link register"]},
    {"question": "Which x86 register is used for the base of data?", "choices": [" EBX", " EAX", " ESI"]},
    {"question": "What is the function of the RDI register in x64 architecture?", "choices": [" Destination index", " Stack pointer", " Base pointer"]},
    {"question": "In x64, what is the purpose of the RSP register?", "choices": [" Stack pointer", " Base pointer", " Source index"]},
    {"question": "In older Intel architecture, which register holds segment information?", "choices": [" AX", " BX", " DS"]},
    {"question": "Which ARM register is used as a scratch register for function arguments?", "choices": [" R0", " R7", " R12"]},
    {"question": "What is the primary function of the RDX register in x64 architecture?", "choices": [" Data register", " Source index", " Accumulator"]},
    {"question": "In x86, which register stores the count for string operations?", "choices": [" ECX", " EAX", " EDX"]},
    {"question": "What register is used for conditional flags in x86 architecture?", "choices": [" EFLAGS", " EIP", " ESI"]},
    {"question": "In ARM, which register holds the conditional flags?", "choices": [" CPSR", " SP", " PC"]},
    {"question": "What does the RIP register in x64 architecture store?", "choices": [" Instruction pointer", " Return address", " Base pointer"]},
    {"question": "In older Intel architecture, what is the purpose of the IP register?", "choices": [" Instruction pointer", " Stack pointer", " Base pointer"]},
    {"question": "Which x86 register is used to point to the top of the stack?", "choices": [" ESP", " EBP", " EAX"]},
    {"question": "In ARM architecture, what is the primary purpose of the R0 register?", "choices": [" Function arguments", " Stack pointer", " Program counter"]},
    {"question": "In 32-bit x86 systems, which register holds the extended flags?", "choices": [" EFLAGS", " EBP", " ESP"]},
    {"question": "Which register in x86 architecture is used for extended division and multiplication?", "choices": [" EDX", " ECX", " ESI"]},
    {"question": "In older Intel architectures, which register points to the instruction to execute?", "choices": [" IP", " AX", " DS"]},
    {"question": "What is the x64 equivalent of the EAX register?", "choices": [" RAX", " RBX", " RCX"]},
    {"question": "In ARM, which register stores the link to the next instruction?", "choices": [" LR", " PC", " SP"]},
    {"question": "What does the x86 register EIP store?", "choices": [" Instruction pointer", " Base pointer", " Stack pointer"]},
    {"question": "In ARM, which register is used for system calls?", "choices": [" R7", " R0", " R3"]},
    {"question": "Which x64 register is used for the base pointer?", "choices": [" RBP", " RAX", " RSI"]},
    {"question": "In 32-bit Linux, which register stores the instruction pointer?", "choices": [" EIP", " EBP", " ESP"]},
    {"question": "What is the 64-bit equivalent of the ESP register?", "choices": [" RSP", " RIP", " RBX"]},
    {"question": "Which x86 register stores the destination index for string operations?", "choices": [" EDI", " ESI", " EBX"]},
    {"question": "In ARM, which register stores the Program Counter?", "choices": [" R15", " R0", " R11"]},
    {"question": "In x86 architecture, what is the purpose of the EBX register?", "choices": [" Base register", " Accumulator", " Stack pointer"]},
    {"question": "What is the role of the ECX register in x86 architecture?", "choices": [" Count register", " Stack pointer", " Base pointer"]},
    {"question": "In ARM, which register is the Program Counter (PC)?", "choices": [" R15", " R13", " R14"]},
    {"question": "In x86, which register is known as the Base Pointer?", "choices": [" EBP", " ESP", " EAX"]},
    {"question": "Which 64-bit register is responsible for holding the base of the stack in x64 architecture?", "choices": [" RSP", " RBP", " RSI"]},
    {"question": "In ARM architecture, which register is used as the Link Register?", "choices": [" LR", " SP", " PC"]},
    {"question": "Which register in x64 architecture is used as the base pointer?", "choices": [" RBP", " RSP", " RAX"]},
    {"question": "Which register in x86 architecture is used as the source index in string operations?", "choices": [" ESI", " EDI", " EBX"]},
    {"question": "In x64 architecture, which register holds the instruction pointer?", "choices": [" RIP", " RSP", " RBX"]},
    {"question": "What is the equivalent of the x86 ECX register in x64?", "choices": [" RCX", " RDX", " RAX"]},
    {"question": "In ARM, which register is used for conditional branches?", "choices": [" CPSR", " R7", " R13"]},
    {"question": "Which x86 register holds the result of I/O operations?", "choices": [" EAX", " ESI", " EDI"]},
    {"question": "In x64, which register is used to pass the first function argument in Linux ABI?", "choices": [" RDI", " RSI", " RCX"]},
    {"question": "Which register holds the flags in x86 architecture?", "choices": [" EFLAGS", " EBP", " ESP"]},
    {"question": "In ARM, which register is responsible for the Current Program Status?", "choices": [" CPSR", " R0", " SP"]},
    {"question": "What does the Intel IP register represent in older architectures?", "choices": [" Instruction Pointer", " Stack Pointer", " Accumulator"]},
    {"question": "Which ARM register holds the return value of a function?", "choices": [" R0", " R7", " R14"]},
    {"question": "In older Intel architectures, which register is known for holding the accumulator?", "choices": [" AX", " BX", " DX"]},
    {"question": "What is the function of the x86 EIP register?", "choices": [" Instruction Pointer", " Stack Pointer", " Base Pointer"]},
    {"question": "Which register in x86 is used for the extended stack pointer?", "choices": [" ESP", " EBP", " EBX"]},
    {"question": "In ARM architecture, which register is used as a stack pointer?", "choices": [" SP", " PC", " LR"]},
    {"question": "Which register in x64 is used to pass the third function argument?", "choices": [" RDX", " RDI", " RSI"]},
    {"question": "Which x86 register is used for holding the result of division?", "choices": [" EDX", " ESI", " EBX"]},
    {"question": "In older Intel architectures, which register represents the code segment?", "choices": [" CS", " DS", " SS"]},
    {"question": "What is the 64-bit equivalent of the ESI register?", "choices": [" RSI", " RDI", " RAX"]},
    {"question": "Which register in x86 is used to point to the top of the stack?", "choices": [" ESP", " EBP", " EAX"]},
    {"question": "In x64, which register is used for the second function argument?", "choices": [" RSI", " RDI", " RCX"]},
    {"question": "What does RDI stand for in x64 architecture?", "choices": [" Destination Index", " Source Index", " Stack Index"]},
    {"question": "What does RSI stand for in x64 architecture?", "choices": [" Source Index", " Stack Index", " Register Stack"]},
    {"question": "What does RAX stand for in x64 architecture?", "choices": [" Accumulator", " Base", " Count"]},
    {"question": "What does RBX stand for in x64 architecture?", "choices": [" Base", " Count", " Destination Index"]},
    {"question": "What does RCX stand for in x64 architecture?", "choices": [" Count", " Accumulator", " Base"]},
    {"question": "What does RDX stand for in x64 architecture?", "choices": [" Data Register", " Accumulator", " Stack Pointer"]},
    {"question": "What does RIP stand for in x64 architecture?", "choices": [" Instruction Pointer", " Base Pointer", " Stack Pointer"]},
    {"question": "What does RBP stand for in x64 architecture?", "choices": [" Base Pointer", " Stack Pointer", " Instruction Pointer"]},
    {"question": "What does RSP stand for in x64 architecture?", "choices": [" Stack Pointer", " Source Pointer", " Base Pointer"]},
    {"question": "What does EAX stand for in x86 architecture?", "choices": [" Extended Accumulator", " Base", " Count"]},
    {"question": "What does EBX stand for in x86 architecture?", "choices": [" Extended Base", " Stack Pointer", " Source Index"]},
    {"question": "What does ECX stand for in x86 architecture?", "choices": [" Extended Count", " Base", " Destination Index"]},
    {"question": "What does EDX stand for in x86 architecture?", "choices": [" Extended Data", " Stack", " Accumulator"]},
    {"question": "What does EBP stand for in x86 architecture?", "choices": [" Extended Base Pointer", " Extended Stack Pointer", " Data Pointer"]},
    {"question": "What does ESP stand for in x86 architecture?", "choices": [" Extended Stack Pointer", " Base Pointer", " Count Register"]},
    {"question": "What does ESI stand for in x86 architecture?", "choices": [" Extended Source Index", " Extended Stack Pointer", " Base Pointer"]},
    {"question": "What does EDI stand for in x86 architecture?", "choices": [" Extended Destination Index", " Extended Data Index", " Source Index"]},
    {"question": "What does LR stand for in ARM architecture?", "choices": [" Link Register", " Local Register", " Load Register"]},
    {"question": "What does SP stand for in ARM architecture?", "choices": [" Stack Pointer", " Source Pointer", " Status Pointer"]},
    {"question": "What does PC stand for in ARM architecture?", "choices": [" Program Counter", " Pointer Count", " Process Count"]},
    {"question": "What does CPSR stand for in ARM architecture?", "choices": [" Current Program Status Register", " Control Program Stack Register", " Condition Pointer Status Register"]},
    {"question": "What does IP stand for in older Intel architectures?", "choices": [" Instruction Pointer", " Stack Pointer", " Data Pointer"]},
    {"question": "What does BP stand for in older Intel architectures?", "choices": [" Base Pointer", " Stack Pointer", " Data Pointer"]},
    {"question": "What does AX stand for in older Intel architectures?", "choices": [" Accumulator", " Base", " Stack"]},
    {"question": "What does BX stand for in older Intel architectures?", "choices": [" Base", " Count", " Accumulator"]},
    {"question": "What does CX stand for in older Intel architectures?", "choices": [" Count", " Base", " Accumulator"]},
    {"question": "What does DX stand for in older Intel architectures?", "choices": [" Data", " Count", " Base"]},
    {"question": "What does DS stand for in older Intel architectures?", "choices": [" Data Segment", " Destination Segment", " Stack Segment"]},
    {"question": "What does SS stand for in older Intel architectures?", "choices": [" Stack Segment", " Source Segment", " Status Segment"]},
    {"question": "What does CS stand for in older Intel architectures?", "choices": [" Code Segment", " Control Segment", " Count Segment"]},
    {"question": "What is the ARM equivalent of the x86 ECX register?", "choices": [" R1", " R0", " R2"]},
    {"question": "What is the ARM equivalent of the x86 EAX register?", "choices": [" R0", " R1", " R3"]},
    {"question": "What is the ARM equivalent of the x86 EDX register?", "choices": [" R2", " R0", " R3"]},
    {"question": "What is the ARM equivalent of the x86 EBX register?", "choices": [" R3", " R4", " R1"]},
    {"question": "What is the ARM equivalent of the x86 ESI register?", "choices": [" R4", " R5", " R3"]},
    {"question": "What is the ARM equivalent of the x86 EDI register?", "choices": [" R5", " R6", " R2"]},
    {"question": "What is the ARM equivalent of the x86 ESP register?", "choices": [" SP", " R7", " LR"]},
    {"question": "What is the ARM equivalent of the x86 EBP register?", "choices": [" R7", " R8", " SP"]},
    {"question": "What is the ARM equivalent of the x64 RAX register?", "choices": [" R0", " R1", " R2"]},
    {"question": "What is the ARM equivalent of the x64 RBX register?", "choices": [" R3", " R4", " R5"]},
    {"question": "What is the ARM equivalent of the x64 RCX register?", "choices": [" R1", " R0", " R2"]},
    {"question": "What is the ARM equivalent of the x64 RDX register?", "choices": [" R2", " R3", " R0"]},
    {"question": "What is the ARM equivalent of the x64 RSI register?", "choices": [" R4", " R5", " R6"]},
    {"question": "What is the ARM equivalent of the x64 RDI register?", "choices": [" R5", " R6", " R7"]},
    {"question": "What is the ARM equivalent of the x64 RSP register?", "choices": [" SP", " LR", " PC"]},
    {"question": "What is the ARM equivalent of the x64 RBP register?", "choices": [" R7", " R6", " SP"]},
    {"question": "What is the ARM equivalent of the x86 EIP register?", "choices": [" PC", " LR", " SP"]},
    {"question": "What is the ARM equivalent of the x86 FLAGS register?", "choices": [" CPSR", " SPSR", " R8"]},
    {"question": "What is the ARM equivalent of the x64 RIP register?", "choices": [" PC", " LR", " SP"]},
    {"question": "What is the ARM equivalent of the x86 LINK register (LR)?", "choices": [" R14", " R13", " R15"]},
    {"question": "What is the ARM equivalent of the x86 STACK POINTER (ESP)?", "choices": [" SP", " R0", " R1"]},
    {"question": "What is the ARM equivalent of the x86 BASE POINTER (EBP)?", "choices": [" FP", " SP", " R4"]},
    {"question": "What is the ARM equivalent of the x86 CONTROL REGISTER (CR0)?", "choices": [" CPSR", " R0", " SP"]},
    {"question": "What is the ARM equivalent of the x64 RFLAGS register?", "choices": [" CPSR", " SPSR", " PC"]},
    {"question": "What is the ARM equivalent of the x86 ESI register?", "choices": [" R6", " R7", " R8"]},
    {"question": "What is the ARM equivalent of the x86 IP register in older Intel architectures?", "choices": [" PC", " LR", " SP"]},
    {"question": "What is the ARM equivalent of the x86 DS register?", "choices": [" R1", " PC", " LR"]},
    {"question": "What is the ARM equivalent of the x86 CS register?", "choices": [" R2", " PC", " SP"]},
    {"question": "What is the ARM equivalent of the x86 DX register?", "choices": [" R3", " R4", " R5"]},
    {"question": "What is the ARM equivalent of the x64 RDI register for passing arguments?", "choices": [" R0", " R1", " R2"]},


]
def randomize_choices(question):
    """Randomize the order of choices and set the correct answer."""
    correct_answer = question["choices"][0]  # Assume the first choice is correct
    random.shuffle(question["choices"])
    question["answer"] = chr(ord('a') + question["choices"].index(correct_answer))
    return question

def ask_question(question_data):
    """Ask a question and return True if the answer is correct, otherwise False."""
    print(question_data["question"])
    for i, choice in enumerate(question_data["choices"]):
        print(f"{chr(ord('a') + i)}) {choice}")
    user_answer = input("Your answer (a/b/c/:) ").lower().strip()

    if user_answer == question_data["answer"]:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer was {question_data['answer']}: {question_data['choices'][ord(question_data['answer']) - ord('a')]}.\n")
        return False

def run_quiz():
    """Run the quiz by asking random questions."""
    print("Welcome to the CPU Register Quiz!")
    random.shuffle(questions)
    score = 0

    for question in questions:
        randomized_question = randomize_choices(question)
        if ask_question(randomized_question):
            score += 1

    print(f"Quiz finished! You got {score} out of {len(questions)} correct.")

if __name__ == "__main__":
    run_quiz()