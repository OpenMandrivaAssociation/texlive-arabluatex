%global tl_name arabluatex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.20
Release:	%{tl_revision}.1
Summary:	ArabTeX for LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/arabluatex
License:	gpl3+ cc-by-sa-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arabluatex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arabluatex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arabluatex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides for LuaLaTeX an ArabTeX-like interface to generate
Arabic writing from an ascii transliteration. It is particularly well-
suited for complex documents such as technical documents or critical
editions where a lot of left-to-right commands intertwine with Arabic
writing. arabluatex is able to process any ArabTeX input notation. Its
output can be set in the same modes of vocalization as ArabTeX, or in
different roman transliterations. It further allows many typographical
refinements. It will eventually interact with some other packages yet to
come to produce from .tex source files, in addition to printed books,
TEI xml compliant critical editions and/or lexicons that can be
searched, analyzed and correlated in various ways.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/lualatex
%dir %{_datadir}/texmf-dist/source/lualatex
%dir %{_datadir}/texmf-dist/tex/lualatex
%dir %{_datadir}/texmf-dist/doc/lualatex/arabluatex
%dir %{_datadir}/texmf-dist/source/lualatex/arabluatex
%dir %{_datadir}/texmf-dist/tex/lualatex/arabluatex
%dir %{_datadir}/texmf-dist/doc/lualatex/arabluatex/samples
%doc %{_datadir}/texmf-dist/doc/lualatex/arabluatex/arabluatex.el
%doc %{_datadir}/texmf-dist/doc/lualatex/arabluatex/arabluatex.pdf
%doc %{_datadir}/texmf-dist/doc/lualatex/arabluatex/samples/al-Jahiz.pdf
%doc %{_datadir}/texmf-dist/doc/lualatex/arabluatex/samples/al-Jahiz.tex
%doc %{_datadir}/texmf-dist/doc/lualatex/arabluatex/samples/exporting.pdf
%doc %{_datadir}/texmf-dist/doc/lualatex/arabluatex/samples/exporting.tex
%doc %{_datadir}/texmf-dist/doc/lualatex/arabluatex/samples/template-01.pdf
%doc %{_datadir}/texmf-dist/doc/lualatex/arabluatex/samples/template-01.tex
%doc %{_datadir}/texmf-dist/source/lualatex/arabluatex/README.md
%doc %{_datadir}/texmf-dist/source/lualatex/arabluatex/README.tex
%doc %{_datadir}/texmf-dist/source/lualatex/arabluatex/arabluatex.dtx
%doc %{_datadir}/texmf-dist/source/lualatex/arabluatex/arabluatex.ins
%doc %{_datadir}/texmf-dist/source/lualatex/arabluatex/makefile
%{_datadir}/texmf-dist/tex/lualatex/arabluatex/arabluatex-patch.sty
%{_datadir}/texmf-dist/tex/lualatex/arabluatex/arabluatex.lua
%{_datadir}/texmf-dist/tex/lualatex/arabluatex/arabluatex.sty
%{_datadir}/texmf-dist/tex/lualatex/arabluatex/arabluatex_fullvoc.lua
%{_datadir}/texmf-dist/tex/lualatex/arabluatex/arabluatex_novoc.lua
%{_datadir}/texmf-dist/tex/lualatex/arabluatex/arabluatex_trans.lua
%{_datadir}/texmf-dist/tex/lualatex/arabluatex/arabluatex_voc.lua
