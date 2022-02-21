{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "f7ff0659",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2fc3eb0a",
   "metadata": {},
   "source": [
    "# Reading File"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "a93084a1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "fname,lname,uid,location\n",
      "rajesh,aaaa,21596,bangalore\n",
      "puja,bbbb,21595,kolar\n",
      "umrah,cccc,21546,mysore\n",
      "anuj,ddddd,21578,nandihills\n",
      "ashish,eeee,21597,krpuram\n",
      "\n"
     ]
    }
   ],
   "source": [
    "with open('1.csv') as i:\n",
    "   f_read=i.read()\n",
    "   print(f_read)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "b2f26e38",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['fname', 'lname', 'uid', 'location']\n",
      "['rajesh', 'aaaa', '21596', 'bangalore']\n",
      "['puja', 'bbbb', '21595', 'kolar']\n",
      "['umrah', 'cccc', '21546', 'mysore']\n",
      "['anuj', 'ddddd', '21578', 'nandihills']\n",
      "['ashish', 'eeee', '21597', 'krpuram']\n"
     ]
    }
   ],
   "source": [
    "w= open('1.csv')\n",
    "read=csv.reader(w)\n",
    "for i in read:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "2ec6e2c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['fname', 'lname', 'uid', 'location']\n",
      "['rajesh', 'aaaa', '21596', 'bangalore']\n",
      "['puja', 'bbbb', '21595', 'kolar']\n",
      "['umrah', 'cccc', '21546', 'mysore']\n"
     ]
    }
   ],
   "source": [
    "# slicing\n",
    "w= open('1.csv')\n",
    "read=csv.reader(w)\n",
    "sli=list(read)\n",
    "# print(sli[1:5])\n",
    "# or\n",
    "for i in sli[:4]:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "b67f50d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "# length\n",
    "w= open('1.csv')\n",
    "read=csv.reader(w)\n",
    "sli=list(read)\n",
    "print(len(sli))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "d6b8c513",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['yamini', 'ashish', 'bangalore', 'kolar', 'mysore', 'nandihills', 'krpuram']\n"
     ]
    }
   ],
   "source": [
    "# append\n",
    "w= open('1.csv')\n",
    "read=csv.reader(w)\n",
    "slicing=list(read)\n",
    "emp_list=['yamini','ashish']\n",
    "for i in slicing[1:]:\n",
    "    emp_list.append(i[3])\n",
    "print(emp_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "c8c367a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['rajesh aaaa', 'puja bbbb', 'umrah cccc', 'anuj ddddd', 'ashish eeee']\n"
     ]
    }
   ],
   "source": [
    "# full name with append\n",
    "w= open('1.csv')\n",
    "read=csv.reader(w)\n",
    "sli=list(read)\n",
    "full_name=[]\n",
    "for i in sli[1:6]:\n",
    "    full_name.append(i[0]+' '+i[1])\n",
    "print(full_name)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b52f162a",
   "metadata": {},
   "source": [
    "# Writing File"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "f2d3f4cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('csv_w.csv','w')as w:          #check the pwd file is there or not\n",
    "    x=csv.writer(w)\n",
    "    x.writerow(['pyhton','java','R','sita'])\n",
    "    x.writerows([['pyhton','java','R'],['apple','banana','coconut'],['biriyani','dosa','idli']])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dcf59628",
   "metadata": {},
   "source": [
    "# Working with pdf file\n",
    "first install PyPDF2 library\n",
    "open your cmd and type command  pip install pypdf2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "9b254d76",
   "metadata": {},
   "outputs": [],
   "source": [
    "import PyPDF2\n",
    "# from PyPDF2 import PdfFileReader\n",
    "with open('WBP.pdf','rb')as pdf_handle:\n",
    "    pdf_reader=PyPDF2.PdfFileReader(pdf_handle)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "abf4aac4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "with open('WBP.pdf','rb')as pdf_handle:\n",
    "    pdf_reader=PyPDF2.PdfFileReader(pdf_handle)\n",
    "    page=pdf_reader.numPages   #numPages is used to find no of pages present in the pdf\n",
    "    print(page)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "3f71c522",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "applications. Quickly drive clicks-and-mortar catalysts for change before \n",
      "vertical architectures. \n",
      "Credibly reintermediate backend ideas for cross-platform models. \n",
      "Continually reintermediate integrated processes through technically sound \n",
      "intellectual capital. Holistically foster superior methodologies without \n",
      "market-driven best practices. Distinctively exploit optimal alignments for intuitive bandwidth. Quickly \n",
      "coordinate e-business applications through revolutionary catalysts for \n",
      "change. Seamlessly underwhelm optimal testing procedures whereas \n",
      "bricks-and-clicks processes. \n",
      "Synergistically evolve 2.0 technologies rather than just in time initiatives. \n",
      "Quickly deploy strategic networks with compelling e-business. Credibly \n",
      "pontiÞcate highly efÞcient manufactured products and enabled data. \n",
      "Dynamically target high-payoff intellectual capital for customized \n",
      "technologies. Objectively integrate emerging core competencies before \n",
      "process-centric communities. Dramatically evisculate holistic innovation \n",
      "rather than client-centric data. Progressively maintain extensive infomediaries via extensible niches. \n",
      "Dramatically disseminate standardized metrics after resource-leveling \n",
      "processes. Objectively pursue diverse catalysts for change for \n",
      "interoperable meta-services. \n",
      "Proactively fabricate one-to-one materials via effective e-business. \n",
      "Completely synergize scalable e-commerce rather than high standards in \n",
      "e-services. Assertively iterate resource maximizing products after leading-\n",
      "edge intellectual capital. Distinctively re-engineer revolutionary meta-services and premium \n",
      "architectures. Intrinsically incubate intuitive opportunities and real-time \n",
      "potentialities. Appropriately communicate one-to-one technology after \n",
      "plug-and-play networks. Quickly aggregate B2B users and worldwide potentialities. Progressively \n",
      "plagiarize resource-leveling e-commerce through resource-leveling core \n",
      "BUSINESS PROPOSAL\n",
      "!3\n"
     ]
    }
   ],
   "source": [
    "import PyPDF2\n",
    "# from PyPDF2 import PdfFileReader\n",
    "with open('WBP.pdf','rb')as pdf_handle:\n",
    "    pdf_reader=PyPDF2.PdfFileReader(pdf_handle)\n",
    "    page_one=pdf_reader.getPage(2)#assigning page number\n",
    "    ex_text=page_one.extractText()#extracting text for assigned page no\n",
    "    print(ex_text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0a8ac428",
   "metadata": {},
   "outputs": [],
   "source": [
    "#     copy pages and append pages to new pdf\n",
    "with open('WBP.pdf','rb')as pdf_handle:\n",
    "    pdf_reader=PyPDF2.PdfFileReader(pdf_handle)\n",
    "    page_one=pdf_reader.getPage(0)\n",
    "    pdf_writer=PyPDF2.PdfFileWriter()\n",
    "    pdf_writer.addPage(page_one)\n",
    "    pdf_output= open('new.pdf','wb')\n",
    "    pdf_writer.write(pdf_output)\n",
    "    pdf_output.close"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "92f9e34b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# read all the text from pdf file\n",
    "with open('WBP.pdf','rb')as pdf_handle:\n",
    "    pdf_reader=PyPDF2.PdfFileReader(pdf_handle)\n",
    "    f = open('WBP.pdf','rb')\n",
    "    text = []\n",
    "    for i in range(pdf_reader.numPages):\n",
    "        page = pdf_reader.getPage(i)    \n",
    "        text.append(page.extractText())\n",
    "    # print(text)#prin all text\n",
    "    print(text[2])#perticular page"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "214dd20c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
