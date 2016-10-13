# Reverse cipher
import sys,pyperclip

__author__ = "Evan Mu"


def main():
    my_message = """Alan Mathison Turing was a British mathematician, logician
    , cryptanalyst, and computer scientist. He was highly influential in the d
    evelopment of computer science, providing a formalisation of the concepts of
     "algorithm" and "computation" with the Turing machine. Turing is widely con
     sidered to be the father of computer science and artificial intelligence. D
     uring World War II, Turing worked for the Government Code and Cypher School
      (GCCS) at Bletchley Park, Britain's codebreaking centre. For a time he was
       head of Hut 8, the section responsible for German naval cryptanalysis. He
        devised a number of techniques for breaking German ciphers, including the
         method of the bombe, an electromechanical machine that could find settin
         gs for the Enigma machine. After the war he worked at the National Physi
         cal Laboratory, where he created one of the first designs for a stored-pr
         ogram computer, the ACE. In 1948 Turing joined Max Newman's Computing Lab
         oratory at Manchester University, where he assisted in the development of
          the Manchester computers and became interested in mathematical biology.
          He wrote a paper on the chemical basis of morphogenesis, and predicted o
          scillating chemical reactions such as the Belousov-Zhabotinsky reaction,
          which were first observed in the 1960s. Turing's homosexuality resulted i
          n a criminal prosecution in 1952, when homosexual acts were still illegal
          in the United Kingdom. He accepted treatment with female hormones (chemical
           castration) as an alternative to prison. Turing died in 1954, just over
           two weeks before his 42nd birthday, from cyanide poisoning. An inquest
           determined that his death was suicide; his mother and some others believed
           his death was accidental. On 10 September 2009, following an Internet
           campaign, British Prime Minister Gordon Brown made an official public
           apology on behalf of the British government for "the appalling way he was
           treated." As of May 2012 a private member's bill was before the House of Lords
            which would grant Turing a statutory pardon if enacted."""

    print("Reverse Cipher")

    translated = reverse_cipher(my_message)
    print(translated)
    # Copy to clipboard
    pyperclip.copy(translated)


def reverse_cipher(plain_text):
    translated = ''

    i = len(plain_text) - 1
    while i >= 0:
        translated = translated + plain_text[i]
        i -= 1

    return translated

if __name__ == '__main__':
    main()



