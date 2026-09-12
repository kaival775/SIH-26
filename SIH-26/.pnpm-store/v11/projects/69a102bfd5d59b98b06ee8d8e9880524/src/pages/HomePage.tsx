import { useEffect } from "react";
import { Link } from "react-router";
import {
  ArrowRight,
  CheckCircle2,
  Code2,
  Cpu,
  Eye,
  FileOutput,
  LockKeyhole,
  Route,
  Sparkles,
} from "lucide-react";
import { BRAND } from "@/config/brand";
import { usePageHeader } from "@/contexts/usePageHeader";
import "./home-page.css";

const flow = [
  { icon: Sparkles, label: "Your request", detail: "Natural language, file, or image" },
  { icon: Route, label: "Auto routing", detail: "Intent selects the right specialist" },
  { icon: Cpu, label: "Local model", detail: "The model swaps into available VRAM" },
  { icon: CheckCircle2, label: "Verified result", detail: "Tools complete and check the work" },
] as const;

const specialists = [
  { name: "General", model: "Qwen", icon: Sparkles, detail: "Reasoning and agent tasks" },
  { name: "Engineer", model: "Qwen", icon: Code2, detail: "Code, APIs, and execution" },
  { name: "Writer", model: "Gemma", icon: FileOutput, detail: "Writing and summaries" },
  { name: "Vision", model: "Qwen-VL", icon: Eye, detail: "Images and OCR" },
] as const;

export default function HomePage() {
  const { setAfterTitle, setEnd } = usePageHeader();

  useEffect(() => {
    setAfterTitle(null);
    setEnd(null);
    return () => {
      setAfterTitle(null);
      setEnd(null);
    };
  }, [setAfterTitle, setEnd]);

  return (
    <main className="indra-home" aria-label={`${BRAND.name} overview`}>
      <section className="indra-hero">
        <div className="indra-hero-copy">
          <div className="indra-kicker"><span /> PRIVATE · LOCAL · ORCHESTRATED</div>
          <h2>{BRAND.tagline}</h2>
          <p>
            {BRAND.name} turns one natural-language request into a complete local workflow.
            It selects a specialist model, uses the required skills and tools, and returns a
            checked result while your data stays on this machine.
          </p>
          <div className="indra-hero-actions">
            <Link className="indra-primary-action" to="/chat">
              Open Command Center <ArrowRight aria-hidden />
            </Link>
            <Link className="indra-secondary-action" to="/models">View model registry</Link>
          </div>
        </div>
        <div className="indra-signal" aria-hidden>
          <span className="indra-signal-ring ring-one" />
          <span className="indra-signal-ring ring-two" />
          <span className="indra-signal-core">I</span>
        </div>
      </section>

      <section className="indra-section" aria-labelledby="flow-heading">
        <div className="indra-section-heading">
          <span>01 / SYSTEM FLOW</span>
          <h3 id="flow-heading">One prompt. The right capability.</h3>
        </div>
        <div className="indra-flow">
          <div className="indra-flow-line" aria-hidden><span /></div>
          {flow.map(({ icon: Icon, label, detail }, index) => (
            <article className="indra-flow-step" key={label}>
              <div className="indra-step-index">0{index + 1}</div>
              <div className="indra-step-icon"><Icon aria-hidden /></div>
              <h4>{label}</h4>
              <p>{detail}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="indra-grid-section">
        <div className="indra-specialists">
          <div className="indra-section-heading">
            <span>02 / SPECIALISTS</span>
            <h3>Purpose-built roles</h3>
          </div>
          <div className="indra-role-grid">
            {specialists.map(({ name, model, icon: Icon, detail }) => (
              <article className="indra-role-card" key={name}>
                <Icon aria-hidden />
                <div><h4>{name}</h4><p>{detail}</p></div>
                <span>{model}</span>
              </article>
            ))}
          </div>
        </div>

        <aside className="indra-privacy-card">
          <LockKeyhole aria-hidden />
          <span>LOCAL BY DESIGN</span>
          <h3>Your information stays within your perimeter.</h3>
          <p>Inference, model routing, file analysis, and tool execution run through the local workbench.</p>
          <ul>
            <li>Admin-key API access</li>
            <li>Local GGUF model serving</li>
            <li>Word, PDF, PowerPoint, and Excel output</li>
          </ul>
        </aside>
      </section>
    </main>
  );
}
