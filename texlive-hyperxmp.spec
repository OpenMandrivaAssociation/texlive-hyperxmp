# revision 31252
# category Package
# catalog-ctan /macros/latex/contrib/hyperxmp
# catalog-date 2013-07-20 10:59:16 +0200
# catalog-license lppl1.3
# catalog-version 2.3b
Name:		texlive-hyperxmp
Version:	2.3b
Release:	1
Summary:	Embed XMP metadata within a LaTeX document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hyperxmp
License:	LPPL1.3
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
well. Version 2.2 of the package added support for the IPTC
Photo Metadata schema. It allows \xmpcomma and \xmpquote to be
used in any hyperxmp option, not only those that require
special treatment of commas. And it introduces an \xmplinesep
macro that controls how multiline fields are represented in the
XMP packet. The package integrates seamlessly with hyperref and
requires virtually no modifications to documents that already
exploit hyperref's mechanisms for specifying PDF metadata. The
current version of hyperxmp can embed the following metadata as
XMP: title, authors, primary author's title or position,
metadata writer, subject/summary, keywords, copyright, license
URL, document base URL, document identifier and instance
identifier, language, source file name, PDF generating tool,
PDF version, and contact telephone number/postal address/email
address/URL. Hyperxmp currently embeds XMP only within PDF
documents; it is compatible with pdflatex, xelatex,
latex+dvipdfm, and latex+dvips+ps2pdf.

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
%doc %{_texmfdistdir}/source/latex/hyperxmp/einstein-xmp.tex
%doc %{_texmfdistdir}/source/latex/hyperxmp/einstein1.png
%doc %{_texmfdistdir}/source/latex/hyperxmp/einstein2.png
%doc %{_texmfdistdir}/source/latex/hyperxmp/gglo-hyxmp.ist
%doc %{_texmfdistdir}/source/latex/hyperxmp/gind-hyxmp.ist
%doc %{_texmfdistdir}/source/latex/hyperxmp/hyperxmp.dtx
%doc %{_texmfdistdir}/source/latex/hyperxmp/hyperxmp.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
