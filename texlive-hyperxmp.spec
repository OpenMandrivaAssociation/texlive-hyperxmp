# revision 23378
# category Package
# catalog-ctan /macros/latex/contrib/hyperxmp
# catalog-date 2011-06-13 21:57:04 +0200
# catalog-license lppl
# catalog-version 1.4
Name:		texlive-hyperxmp
Version:	1.4
Release:	2
Summary:	Embed XMP metadata within a LaTeX document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hyperxmp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyperxmp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyperxmp.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyperxmp.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
XMP (eXtensible Metadata Platform) is a mechanism proposed by
Adobe for embedding document metadata within the document
itself. The metadata is designed to be easy to extract, even by
programs that are oblivious to the document's file format. Most
of Adobe's applications store XMP metadata when saving files.
Now, with the hyperxmp package, it is trivial for LaTeX
document authors to store XMP metadata in their documents as
well. Hyperxmp integrates seamlessly with hyperref and requires
virtually no modifications to documents that already exploit
hyperref's mechanisms for specifying PDF metadata. The current
version of hyperxmp can embed the following metadata as XMP:
author, title, subject, keywords, copyright, and license URL.
hyperxmp currently embeds XMP only within PDF documents but is
compatible with pdflatex, xelatex, latex+dvipdfm, and
latex+dvips+ps2pdf.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hyperxmp/hyperxmp.sty
%doc %{_texmfdistdir}/doc/latex/hyperxmp/README
%doc %{_texmfdistdir}/doc/latex/hyperxmp/hyperxmp.pdf
#- source
%doc %{_texmfdistdir}/source/latex/hyperxmp/hyperxmp.dtx
%doc %{_texmfdistdir}/source/latex/hyperxmp/hyperxmp.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
